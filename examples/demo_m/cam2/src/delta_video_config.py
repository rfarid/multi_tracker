class Config:
    def __init__(self):
        self.basename = 'delta_video'
        self.directory = '~/demo_m/cam2/data'
        #self.topics = ['/multi_tracker/2/delta_video',]
        self.topics = ['/multi_tracker/2/delta_video','/multi_tracker/2/contours',]
        self.record_length_hours = 1
