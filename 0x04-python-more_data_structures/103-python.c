#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", (size > 10) ? 10 : size);
    for (i = 0; i < ((size > 10) ? 10 : size); i++)
    {
        printf(" %02x", (unsigned char)str[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < Py_SIZE(p); i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
