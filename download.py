import requests
import progressbar

namuwiki_dump_link = "https://cdn-us.mu-star.net/wikidb/namuwiki180326.7z"

print(" [x] Start downloading Namuwiki Dump File")

# Create Local filename
local_filename = "namuwiki_dump_link".split('/')[-1]

# Initialize Progress Bar
bar = progressbar.ProgressBar(
    maxval=int(1.3e+6), widgets=[
        progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])


# Download file with stream
r = requests.get(namuwiki_dump_link, stream=True)
bar.start()
i = 0
with open(local_filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            bar.update(int(i*1.024+1))
            i = i + 1
            f.flush()

bar.finish()


print(" [x] Finish downloading Namuwiki Dump File")
