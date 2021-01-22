import os
# permission bit 775 for directories
os.umask(0o002) 


c = get_config()


# memory
c.NotebookApp.ResourceUseDisplay.mem_limit = 4 *1024*1024*1024

# cpu
c.NotebookApp.ResourceUseDisplay.track_cpu_percent = True
c.NotebookApp.ResourceUseDisplay.cpu_limit = 16