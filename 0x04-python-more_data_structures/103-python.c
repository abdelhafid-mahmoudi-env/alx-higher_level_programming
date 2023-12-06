#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Print basic info about Python bytes objects
 * @p: PyObject representing bytes object
 */
void print_python_bytes(PyObject *p)
{
    long int byte_size;
    int i;
    char *byte_str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p) && !PyByteArray_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    byte_str = PyBytes_AsString(p);
    byte_size = PyBytes_Size(p);
    printf("  size: %li\n", byte_size);
    printf("  trying string: %s\n", byte_str);
    if (byte_size < 10)
        printf("  first %li bytes:", byte_size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= byte_size && i < 10; i++)
        printf(" %02hhx", byte_str[i]);

    printf("\n");
}

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject representing a list
 */
void print_python_list(PyObject *p)
{
    long int list_size = PyList_Size(p);
    int i;
    PyListObject *list_obj = (PyListObject *)p;
    const char *element_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated = %li\n", list_obj->allocated);
    for (i = 0; i < list_size; i++)
    {
	PyObject *element = list->ob_item[i];
        element_type = element->ob_type->tp_name;
        printf("Element %i: %s\n", i, element_type);
        if (strcmp(element_type, "bytes") == 0)
            print_python_bytes(list_obj->ob_item[i]);
    }
}
