/*Declare the photo's index at the start for the cyclePhotos function */
var photoIndex = 1;
/* Declare an empty array that will be filled with the sols and their cameras */
var solCams = [];

function goodSols() {
    /* Query the NASA API's manifest to get a list of sols and their cameras */
    var request = new XMLHttpRequest();
    var url = "https://api.nasa.gov/mars-photos/api/v1/manifests/curiosity?api_key=BHZ0k33CIapBdz918u2X0mVfmAvEul1dUTOEC9Hs"
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.dir(JSON.parse(this.responseText));
            fillArray(JSON.parse(this.responseText));
        }
    };
    request.open("GET", url, true);
    request.send();
}

function fillArray(manifest) {
    /* Fill the solCams array with key value pairs of the sols and their cameras */
    for (i = 0; i < manifest.photo_manifest.photos.length; i++) {
        /* Increment through the sols and add them to the solCams array */
        var sol = manifest.photo_manifest.photos[i].sol;
        var cams = manifest.photo_manifest.photos[i].cameras;
        solCams.push([sol, cams]);
    }
}

function checkSol(sol) {
    var picsAvalible = false;
    for (var i = 0; i < solCams.length; i++) {
        if (sol == solCams[i][0]) {
            picsAvalible = true;
        }
    }
    if (picsAvalible == true) {
        for (var i = 0; i < solCams[sol][1].length; i++) {
            var opt = document.createElement("option");
            opt.value = solCams[sol][1][i];
            /* Change inner html based on which camera it is */
            if (solCams[sol][1][i] == "FHAZ") {
                opt.innerHTML = "Front Hazard Avoidance Camera";
            }
            else if (solCams[sol][1][i] == "RHAZ") {
                opt.innerHTML = "Rear Hazard Avoidance Camera";
            }
            else if (solCams[sol][1][i] == "MAST") {
                opt.innerHTML = "Mast Camera";
            }
            else if (solCams[sol][1][i] == "CHEMCAM") {
                opt.innerHTML = "Chemistry and Camera Complex";
            }
            else if (solCams[sol][1][i] == "MAHLI") {
                opt.innerHTML = "Mars Hand Lens Imager";
            }
            else if (solCams[sol][1][i] == "MARDI") {
                opt.innerHTML = "Mars Descent Imager";
            }
            else if (solCams[sol][1][i] == "NAVCAM") {
                opt.innerHTML = "Navigation Camera";
            }
            document.getElementById("cameras").appendChild(opt);
        }
    }
    else {
        window.alert("The sol that you selected does not have any pictures associated with it. Please choose a different sol.");
        document.getElementById("sol").value = "";
    }
}

function getPhotos() {
    /* Query the NASA API and return with the photos */
    /* Delete the photos already present */
    var oldPics = document.getElementsByClassName("pictures");
    console.dir(oldPics);
    for (var i = 0; i < oldPics.length; i++) {
        oldPics[i].remove();
    }
    var request = new XMLHttpRequest();
    
    /* Access the DOM and get the values from the form */
    var sol = document.getElementById("sol").value;
    var camera = document.getElementById("cameras").value;
    /* Creates the url based on the user selected sol and camera */
    var url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=" + sol + "&camera=" + camera + "&api_key=BHZ0k33CIapBdz918u2X0mVfmAvEul1dUTOEC9Hs";
    /* Function for recieving data */
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var obj = JSON.parse(this.responseText);
            createPhoto(obj.photos);
        }
    };
    /* Send the request to the API */
    request.open("GET", url, true);
    request.send();
}

function createPhoto(photos) {
    /* Creates the HTML img elements for all the returned photos */
    for (var i = 0; i < photos.length; i++) {
        var img = document.createElement("img");
        /* Assign them a collective class for css, and a unique id */
        img.className = "pictures";
        img.id = i + 1;
        img.src = photos[i].img_src;
        document.getElementById("imageContainer").appendChild(img);
    }
    cyclePhotos(1);
}

function arrowPics(n) {
    /* Increment the photo slideshow when the arrows are clicked */
    cyclePhotos(photoIndex += n);
}

function cyclePhotos(n) {
    /* Changes the photos, displaying the current one and hiding the rest */
    var photos = document.getElementsByClassName("pictures");
    /* Update the photoIndex based on the given n */
    if (n > photos.length) {
        photoIndex = 1;
    }
    else if (n < 1) {
        photoIndex = photos.length;
    }
    else {
        photoIndex = n;
    }
    /* For loop that hides all the photos except the current one */
    for (var i = 0; i < photos.length; i++) {
        if (i == photoIndex - 1) {
            photos[i].style.display = "block";
        }
        else {
            photos[i].style.display = "none";
        }
    }
}