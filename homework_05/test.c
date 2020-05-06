#include <Python.h>


PyObject *matmul(PyObject* self, PyObject* args)
{
	PyObject *mat1;
	PyObject *mat2;
	
	if (!PyArg_ParseTuple(args, "OO", &mat1, &mat2))
	{
		return NULL
	}
	
	long len = PyList_Size(mat1);
	
	return Py_BuildValue("l", len)
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
