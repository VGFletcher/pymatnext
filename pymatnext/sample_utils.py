class NullComm():
    """Fake alternative to mpi4py.MPI.Comm for serial run, which implements needed subset
    of mpi4py.MPI.Comm methods
    """
    def __init__(self):
        self.size = 1
        self.rank = 0

    def bcast(self, data, root=None):
        return data

    def scatter(self, l_data, root=None):
        return l_data[0]

    def gather(self, data, root=None):
        return [data]

    def allreduce(self, data, op=None):
        return data

    def Allgatherv(self, sendbuf, recvbuf):
        assert sendbuf == MPI.IN_PLACE
        return

class MPI:
    """Fake alternative to mpi4py.MPI for serial runs, which implements necessary subset of
    symbols and methods
    """
    COMM_WORLD = NullComm()
    COMM_SELF = None

    SUM = None
    IN_PLACE = -1
    INT64 = 1
    DOUBLE = 2

    def Finalize():
        return
