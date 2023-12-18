#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to the PyObject representing the bytes object.
 */
void print_python_bytes(PyObject *p)
{
	size_t size, i;
	char *string;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	string = ((PyBytesObject *)(p))->ob_sval;
	size = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", size, string);
	size >= 10 ? size = 10 : size++;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size - 1; i++)
		printf("%02hhx ", string[i]);
	printf("%02hhx\n", string[i]);
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: A pointer to the PyObject representing the float object.
 */
void print_python_float(PyObject *p)
{
	char *string;
	double value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)(p))->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: A pointer to the PyObject representing the list object.
 */
void print_python_list(PyObject *p)
{
	size_t allocated, size, i;
	const char *type_name;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, allocated);
	for (i = 0; i < size; i++)
	{
		type_name = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
		!strcmp(type_name, "bytes") ? print_python_bytes(list->ob_item[i]) : (void)type_name;
		!strcmp(type_name, "float") ? print_python_float(list->ob_item[i]) : (void)type_name;
	}
}

