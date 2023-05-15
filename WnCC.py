# Python program to find
# maximal Bipartite matching.
import numpy as np

class GFG:
	def __init__(self,graph):
		
		# residual graph
		self.graph = graph
		self.ppl = len(graph)
		self.jobs = len(graph[0])

	# A DFS based recursive function
	# that returns true if a matching
	# for vertex u is possible
	def bpm(self, u, matchR, seen):

		# Try every job one by one
		for v in range(self.jobs):

			# If applicant u is interested
			# in job v and v is not seen
			if self.graph[u][v] and seen[v] == False:
				
				# Mark v as visited
				seen[v] = True

				'''If job 'v' is not assigned to
				an applicant OR previously assigned
				applicant for job v (which is matchR[v])
				has an alternate job available.
				Since v is marked as visited in the
				above line, matchR[v] in the following
				recursive call will not get job 'v' again'''
				if matchR[v] == -1 or self.bpm(matchR[v],
											matchR, seen):
					matchR[v] = u
					return True
		return False

	# Returns maximum number of matching
	def maxBPM(self):
		'''An array to keep track of the
		applicants assigned to jobs.
		The value of matchR[i] is the
		applicant number assigned to job i,
		the value -1 indicates nobody is assigned.'''
		matchR = [-1] * self.jobs
		
		# Count of jobs assigned to applicants
		result = 0
		for i in range(self.ppl):
			
			# Mark all jobs as not seen for next applicant.
			seen = [False] * self.jobs
			
			# Find if the applicant 'u' can get a job
			if self.bpm(i, matchR, seen):
				result += 1
		return result,matchR


Par_no = int(input())

Par=[]

# print("Give Applicant Details")

for i in range(Par_no):
	Par.append(input().split()[-5:])
	# storing participant details in a list
	
# print(Par)

Job_no = int(input())

Jobs=[]

# print("Give Job Details")

for i in range(Job_no):
	
	Jobs+=(input().split()[-5:])
	
    # Taking job details
	
matrix=np.array(Par)
matrix1=np.array(Par)

for i in range(Job_no-1):
	
    matrix=np.concatenate((matrix,matrix1),axis=1)

    #making the matrix array size compatible with the job array size

matrix=matrix.astype(int)

# print(matrix)

Jobs=np.array(Jobs).astype(int)

for i in range(Par_no):
	
    matrix[i] = (matrix[i]>=Jobs) #comparing the 2 arrays

    for j in np.where(Jobs==0):
	    
        matrix[i][j]=0

print(matrix)

g=GFG(matrix)

x,y=g.maxBPM()

# print(x)

#print(y)

no_of_projects = 0
for i in range(Job_no):
    flag = True
    for j in range(5):
        if(y[5*i + j] == -1 and jobs_levels[5*i+j] != 0):
            flag = False
    if(flag == True):
        no_of_projects += 1

print(no_of_projects)

# print(Jobs)
	



#print ("Maximum number of applicants that can get job is %d " % g.maxBPM())

# This code is contributed by Geeks for Geeks
 
