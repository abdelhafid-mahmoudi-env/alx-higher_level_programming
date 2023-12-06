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
    printf("  size: %li\n", PyBytes_Size(p));
    printf("  trying string: %s\n", byte_str);
    if (PyBytes_Size(p) < 10)
        printf("  first %li bytes:", PyBytes_Size(p) + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= PyBytes_Size(p) && i < 10; i++)
        printf(" %02hhx", byte_str[i]);

    printf("\n");
}

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject representing a list
 */
void print_python_list(PyObject *p)
{
    int i;
    PyListObject *list_obj = (PyListObject *)p;
    PyObject *element;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", PyList_Size(p));
    printf("[*] Allocated = %li\n", list_obj->allocated);
    for (i = 0; i < PyList_Size(p); i++)
    {
	element = list_obj->ob_item[i];
        printf("Element %i: %s\n", i, element->ob_type->tp_name);
        if (strcmp(element->ob_type->tp_name, "bytes") == 0)
            print_python_bytes(element);
    }
}
