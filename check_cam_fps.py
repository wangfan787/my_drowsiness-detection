
# coding: utf-8

# In[ ]:


import time

def check_fps(prev_time) :
    cur_time = time.time() #以秒为单位导入当前时间
    one_loop_time = cur_time - prev_time
    prev_time = cur_time
    fps = 1/one_loop_time
    return prev_time, fps

