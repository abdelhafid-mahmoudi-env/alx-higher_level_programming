#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    char *str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", (size > 10) ? 10 : size);
    for (Py_ssize_t i = 0; i < ((size > 10) ? 10 : size); i++)
    {
        printf(" %02x", (unsigned char)str[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
