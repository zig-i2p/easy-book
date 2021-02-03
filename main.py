# import os

# os.system('poetry run jupyter server')
import nbformat
from nbclient import NotebookClient
from enterprise_gateway.services.kernels.remotemanager import RemoteKernelManager

with open("my_notebook.ipynb") as fp:
    test_notebook = nbformat.read(fp, as_version=4)

client = NotebookClient(nb=test_notebook, kernel_manager_class=RemoteKernelManager)
client.execute()