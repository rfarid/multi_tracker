class Config:
    def __init__(self):
        self.basename = 'delta_video'
        self.directory = '~/demo_m/cam1/data'
        self.topics = ['/multi_tracker/1/delta_video',]
        self.record_length_hours = 1
