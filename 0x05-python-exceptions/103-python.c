#include <Python.h>
#include <stdio.h>

/**
 * print_float_info - Prints information about a PyFloatObject.
 * @p: A pointer to the PyObject representing the float object.
 */
void print_float_info(PyObject *p)
{
    double value = 0;
    char *str_value = NULL;

    fflush(stdout);
    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    value = ((PyFloatObject *)p)->ob_fval;
    str_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str_value);
    PyMem_Free(str_value);
}

/**
 * print_bytes_info - Prints information about a PyBytesObject.
 * @p: A pointer to the PyObject representing the bytes object.
 */
void print_bytes_info(PyObject *p)
{
    Py_ssize_t size = 0, i = 0;
    char *data = NULL;

    fflush(stdout);
    printf("[.] bytes object info\n");
    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);
    data = ((PyBytesObject *)p)->ob_sval;
    printf("  trying string: %s\n", data);
    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
    while (i < size + 1 && i < 10)
    {
        printf(" %02hhx", data[i]);
        i++;
    }
    printf("\n");
}

/**
 * print_list_info - Prints information about a PyListObject.
 * @p: A pointer to the PyObject representing the list object.
 */
void print_list_info(PyObject *p)
{
    Py_ssize_t size = 0;
    PyObject *item;
    int i = 0;

    fflush(stdout);
    printf("[*] Python list info\n");
    if (PyList_CheckExact(p))
    {
        size = PyList_GET_SIZE(p);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
        while (i < size)
        {
            item = PyList_GET_ITEM(p, i);
            printf("Element %d: %s\n", i, item->ob_type->tp_name);
            if (PyBytes_CheckExact(item))
                print_bytes_info(item);
            else if (PyFloat_CheckExact(item))
                print_float_info(item);
            i++;
        }
    }
    else
        printf("  [ERROR] Invalid List Object\n");
}


