#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints python object list
 * @p: pointer to list
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i, list_size = Py_SIZE(p);
	int allocd = ((PyListObject *)p)->allocated;
	PyObject list_ob;
	const char *type_name;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", allocd);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %d:", i);
		list_ob = PyList_GetItem(p, i);
		type_name = Py_TYPE(list_ob)->tp_name;
		printf("%s\n", type_name;
	}
}
