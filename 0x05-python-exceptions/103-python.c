#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list - Print information about a Python list object.
 * @p: A pointer to the PyObject representing the list.
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t i, size, allocated;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: A pointer to the PyObject representing the bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first %ld bytes: ", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)bytes_str[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: A pointer to the PyObject representing the float object.
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

