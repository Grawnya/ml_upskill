from bing_image_downloader import downloader

def download_images(request):

    """Store downloaded images in a directory.

        Parameters:

    request: list of queries to search for

        # Return: Images downloaded that match request

        """

    downloader.download(request, 
                        limit=20, 
                        output_dir='images', 
                        force_replace=False)
    

requests = ['laptop computer', 'computer monitor', 'computer mouse', 'soccer ball', 'bee', 'locomotive train', 'letter m', 'letter t']

for request in requests:
    download_images(request)