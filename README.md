# Infinite Docker Storage

## Notes

* Although Docker hub does not limit the size of the image, after 10GB there are issues that arise when pulling the image
* After 7GB (to be on the safe side) I would create a new REPO and put data in there.
* Ive read that people have had images up to 20GB in size but lets stay safe :)

## Directions
1. Install Docker

`https://docs.docker.com/engine/install/`

2. Make a Docker Hub account and create a new repo

3. Enter your info in your respective startup file (bat for windows sh for linux/mac)

4. Upload your files 

5. Upon Succesful completion your image will be posted to docker hub 

6. Pull your docker image with this command
`docker pull <repo_path>:savefiles`

7. Run with this command 

`docker run -p 8000:8000 <image_id>`

8. Navigate to localhost:8000

9. View your files in the uploads directory

