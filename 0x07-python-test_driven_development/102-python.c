#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: PyObject string object.
 */
void print_python_string(PyObject *p)
{
    /* Check if the object is a valid string */
    if (!PyUnicode_Check(p))
    {
        printf("[.] string object info\n  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UNICODE *unicode = PyUnicode_AsUnicode(p);
    int is_ascii = PyUnicode_IS_ASCII(p);

    printf("[.] string object info\n");
    printf("  type: %s\n", is_ascii ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", unicode);
}
