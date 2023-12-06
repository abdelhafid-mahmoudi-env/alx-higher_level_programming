#include <Python.h>

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *string;
    PyObject *bytes;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)string[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        }
    }
}


