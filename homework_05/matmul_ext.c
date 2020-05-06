#include <Python.h>


PyObject *matmul(PyObject* self, PyObject* args)
{
	PyObject *matrix1;
	PyObject *matrix2;
	
	if (!PyArg_ParseTuple(args, "OO", &matrix1, &matrix2))
	{
		printf("ERROR: Faild to parse arguments\n");
		return NULL;
	}
	
	long elem;
	long row1 = PyList_Size(matrix1);
	long col1 = PyList_Size(PyList_GetItem(matrix1, 0));
	long col2 = PyList_Size(PyList_GetItem(matrix2, 0));
	long row2 = PyList_Size(matrix2);

	if (col1 != row2)
	{
		printf("ERROR: Matrices cannot be multiplied\n");
		return PyExc_ValueError;
	}

	PyObject *result = PyList_New(0);
	PyObject *tmp = PyList_New(0);

	for (int i = 0; i < row1; i++)
	{
		for (int j = 0; j < col2; j++)
		{
			elem = 0;
			for (int k = 0; k < col1; k++)
			{
				PyObject *v1 = PyList_GetItem(PyList_GetItem(matrix1, i), k);
				PyObject *v2 = PyList_GetItem(PyList_GetItem(matrix2, k), j);
				elem += PyLong_AsLong(v1) * PyLong_AsLong(v2);
			}
			PyList_Append(tmp, Py_BuildValue("i", elem));
		}
		PyObject *result_row = PyList_GetSlice(tmp, i * col2, i * col2 + col2);
		PyList_Append(result, result_row);
	}
	return Py_BuildValue("O", result);
}

static PyMethodDef methods[] = {
	{"matrixmul", matmul, METH_VARARGS, "matrix multiplication"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef matmodule = {
	PyModuleDef_HEAD_INIT, "matmul",
	NULL, -1, methods
};

PyMODINIT_FUNC PyInit_matrix(void) {
    return PyModule_Create(&matmodule);
}
