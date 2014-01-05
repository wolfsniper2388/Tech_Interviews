''' Pytables requirement:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/
    Download:
    (1) hdf5: http://www.hdfgroup.org/HDF5/release/obtain5.html#obtain
    (2) numpy: http://www.lfd.uci.edu/~gohlke/pythonlibs/
    (3) numexpr: http://www.lfd.uci.edu/~gohlke/pythonlibs/
    (4) Pytables: http://www.lfd.uci.edu/~gohlke/pythonlibs/

'''

import tables
class Ut_tests_run(tables.IsDescription):
    id_tag=tables.StringCol(64)
    cmd=tables.StringCol(64)
    exit_status=tables.UInt16Col()
handler=tables.openFile("test1.h5", mode="w")
group=handler.createGroup("/", 'ut_group', 'Unit Test Suite 3.0 ut_tests_run_group')
table=handler.createTable(group, 'ut_table', Ut_tests_run, "UT run details")
row=table.row
print row
tlist=[('001','./fg_test.bin 1', 0),('002','./fg_test.bin 2', 1),('003','./fg_test.bin 3', 0) ]
for t in tlist:
    row['id_tag']=t[0]
    row['cmd']=t[1]
    row['exit_status']=t[2]
    row.append()
table.flush()
#handler.close()

table=handler.root.ut_group.ut_table
results=[r['exit_status'] for r in table.iterrows()]
print results