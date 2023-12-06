#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytesObj;
    char *str;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytesObj = (PyBytesObject *)p;
    PyBytes_AsStringAndSize(p, &str, &size);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %li bytes:", (size < 10) ? size + 1 : 10);

    for (i = 0; i < size && i < 10; i++)
        printf(" %02hhx", str[i]);

    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *listObj;
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");

    size = PyList_Size(p);
    listObj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", listObj->allocated);

    for (i = 0; i < size; i++)
    {
        element = listObj->ob_item[i];
        const char *type = Py_TYPE(element)->tp_name;

        printf("Element %li: %s\n", i, type);

        if (strcmp(type, "bytes") == 0)
            print_python_bytes(element);
    }
}

