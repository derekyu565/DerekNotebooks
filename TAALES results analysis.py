#!/usr/bin/env python
# coding: utf-8

# ### Printing out the columns

# In[103]:


import pandas as pd
import matplotlib.pyplot as plt

resultsComments = pd.read_csv('taalesComments/results.csv')
resultsComments = resultsComments.drop(['Word Count','Filename'], axis=1)
indexCoverageComments = pd.read_csv('taalesComments/results_index_coverage.csv')
indexCoverageComments = indexCoverageComments.drop(['Filename'], axis=1)

print('Results:\n',resultsComments.columns,'\n\n\nIndex Coverage:\n',indexCoverageComments.columns)


# ### Barplot of the results on Comments

# In[104]:


ax=resultsComments.plot.barh(legend=None)
ax.set_title("TAALES Results on Comments")
ax.legend(bbox_to_anchor=(1.0, 1.0))
bx=indexCoverageComments.plot.barh(legend=None)
bx.set_title("TAALES Inex Coverage Results on Comments")
bx.legend(bbox_to_anchor=(1.0, 1.0))

#plt.savefig('Comments.png')


# In[105]:


resultsPosts = pd.read_csv('taalesPosts/results.csv')
resultsPosts = resultsPosts.drop(['Word Count','Filename'], axis=1)
indexCoveragePosts = pd.read_csv('taalesPosts/results_index_coverage.csv')
indexCoveragePosts = indexCoveragePosts.drop(['Filename'], axis=1)

print('Results:\n',resultsPosts.columns,'\n\n\nIndex Coverage:\n',indexCoveragePosts.columns)


# In[107]:


cx=resultsPosts.plot.barh(legend=None)
cx.set_title("TAALES Results on Posts")
cx.legend(bbox_to_anchor=(1.0, 1.0))
dx=indexCoveragePosts.plot.barh(legend=None)
dx.set_title("TAALES Inex Coverage Results on Posts")
dx.legend(bbox_to_anchor=(1.0, 1.0))

#plt.savefig('Comments.png')

plt.show()
