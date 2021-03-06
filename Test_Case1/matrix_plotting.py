#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# USAGE:

# PREAMBLE:

from plotting_functions import *
import sys
import os

avg_file = sys.argv[1]
std_file = sys.argv[2]
#start = int(sys.argv[1])
#end = int(sys.argv[2])
#step = int(sys.argv[3])
system = sys.argv[3]

symmetric = True

change_dir = os.chdir

my_cmap = plt.cm.get_cmap('jet')
avg_data = np.loadtxt(avg_file)
std_data = np.loadtxt(std_file)

if symmetric:
	nRes = len(avg_data)
	for i in range(nRes-1):
		for j in range(i+1,nRes):
			avg_data[j][i] = avg_data[i][j]
			std_data[j][i] = std_data[i][j]

matrix2d(avg_data,'Nucleic Selection','Protein Residue Number','Distance','avg.%s' %(system),'%03d.%03d.pro-ssRNA' %(1,5),cb_units='$\AA$',plt_title='Avg COM-COM Distance (Traj %03d - %03d)' %(1,5),vmax=45.0,xlim=(0,451),ylim=(0,451))
matrix2d(std_data,'Nucleic Selection','Protein Residue Number','Standard Deviation of Distance','stdev.%s' %(system),'%03d.%03d.pro-ssRNA' %(1,5),cb_units='$\AA$',plt_title='St. Dev. COM-COM Distance (Traj %03d - %03d)' %(1,5),vmax=6.0,xlim=(0,451),ylim=(0,451))


#j = 0
#for i in range(start,end,step):
#	j += step
#	change_dir('%03d.%03d.distance_matrix' %(i,j))
#	avg_file = '%03d.%03d.%s.avg_dist_mtx.dat' %(i,j,system)
#	std_file = '%03d.%03d.%s.stdv_dist_mtx.dat' %(i,j,system)
#	
#	avg_data = np.loadtxt(avg_file)
#	std_data = np.loadtxt(std_file)
#
#	matrix2d(avg_data,'Nucleic Selection','Protein Residue Number','Distance','avg.%s' %(system),'%03d.%03d.pro-ssRNA.' %(i,j),cb_units='$\AA$',plt_title='Avg COM-COM Distance (Traj %03d - %03d)' %(i,j))
#	matrix2d(std_data,'Nucleic Selection','Protein Residue Number','Standard Deviation of Distance','stdev.%s' %(system),'%03d.%03d.pro-ssRNA.' %(i,j),cb_units='$\AA$',plt_title='St. Dev. COM-COM Distance (Traj %03d - %03d)' %(i,j))
#
#
#	plt.pcolor(avg_data,cmap=my_cmap,vmin=0.001,vmax=15)
#	cb1 = plt.colorbar(extend='max',cmap=my_cmap)
#	cb1.set_label(r'Average Distance ($\AA$)' )
#	plt.title('Average COM-COM Distance (Traj %03d - %03d)' %(i,j))
#	plt.ylabel(r'Protein Residue Number', size=14)
#	plt.ylim((0,451))
#	plt.xlabel(r'Nucleic Selection', size=14)
#	plt.savefig('avg.%s.%03d.%03d.pcolor.png'%(system,i,j),dpi=300)
#	plt.close()
#
#	plt.pcolor(std_data,cmap=my_cmap,vmin=0.001,vmax=6.0)
#	cb1 = plt.colorbar(extend='max',cmap=my_cmap)
#	cb1.set_label(r'Standard Deviation of Distance ($\AA$)')
#	plt.title('Standard Dev. COM-COM Distance (Traj %03d - %03d)' %(i,j))
#	plt.ylabel(r'Protein Residue Number', size=14)
#	plt.ylim((0,451))
#	plt.xlabel(r'Nucleic Selection', size=14)
#	plt.savefig('stdev.%s.%03d.%03d.pcolor.png'%(system,i,j),dpi=300)
#	plt.close()
#
#	print i, j
#
#	change_dir('..')

