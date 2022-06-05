#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - prints
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
size_t s, i = 0;
PyObject *obj;
s = PyList_Size(p);
printf("[*] Size of the Python List = %zu\n", s);
printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
while (i < s)
{
obj = PyList_GET_ITEM(p, i);
printf("Element %zu: %s\n", i, Py_TYPE(obj)->tp_name);
i++;
}
}
