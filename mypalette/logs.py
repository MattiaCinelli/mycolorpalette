import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M',
                    filename='my_palette.log',
                    filemode='w')

# Define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Set a format which is simpler for console use
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-6s: %(message)s', datefmt='%H:%M')

# Tell the handler to use this format
console.setFormatter(formatter)

# Add the handler to the root logger
logging.getLogger('').addHandler(console)
# Disable matplotlib.font_manager debug messages
logging.getLogger('matplotlib.font_manager').disabled = True# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M',
                    filename='my_palette.log',
                    filemode='w')

# Define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Set a format which is simpler for console use
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-6s: %(message)s', datefmt='%H:%M',)

# Tell the handler to use this format
console.setFormatter(formatter)

# Add the handler to the root logger
logging.getLogger('').addHandler(console)
