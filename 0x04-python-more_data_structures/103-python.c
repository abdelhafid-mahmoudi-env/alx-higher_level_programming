#include <Python.h>

void print_python_set(PyObject *p)
{
    long int size;
    int i;
    PyObject *set_iterator;

    printf("[*] Python set info\n");
    if (!PySet_Check(p))
    {
        printf("[ERROR] Invalid Set Object\n");
        return;
    }

    size = PySet_Size(p);
    printf("[*] Size of the Python Set = %li\n", size);

    set_iterator = PyObject_GetIter(p);
    if (set_iterator != NULL)
    {
        PyObject *set_item;
        printf("Elements:");

        while ((set_item = PyIter_Next(set_iterator)) != NULL)
        {
            PyObject *repr = PyObject_Str(set_item);
            const char *str = PyUnicode_AsUTF8(repr);
            printf(" %s", str);

            Py_DECREF(set_item);
            Py_DECREF(repr);
        }
        printf("\n");

        Py_DECREF(set_iterator);
    }
}

void print_python_tuple(PyObject *p)
{
    long int size;
    int i;

    printf("[*] Python tuple info\n");
    if (!PyTuple_Check(p))
    {
        printf("[ERROR] Invalid Tuple Object\n");
        return;
    }

    size = PyTuple_Size(p);
    printf("[*] Size of the Python Tuple = %li\n", size);

    printf("Elements:");
    for (i = 0; i < size; i++)
    {
        PyObject *tuple_item = PyTuple_GetItem(p, i);
        PyObject *repr = PyObject_Str(tuple_item);
        const char *str = PyUnicode_AsUTF8(repr);
        printf(" %s", str);

        Py_DECREF(repr);
    }
    printf("\n");
}
