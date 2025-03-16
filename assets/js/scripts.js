const covers = [
  "/assets/Mountain.jpg",
  "/assets/Abel.jpg",
  "/assets/Beach.jpg",
  "/assets/Glaciers.jpg",
  "/assets/Sunrise.jpg",
  "/assets/geology.JPG",
  "/assets/stars.jpg",
  "/assets/canyon.JPG"

];

let currentCover = 0;

function rotateCover() {
  const coverElement = document.getElementById('cover-photo');
  if (!coverElement) {
    console.error("Element with id 'cover-photo' not found!");
    return;
  }

  currentCover = (currentCover + 1) % covers.length;
  console.log("Changing cover to:", covers[currentCover]);
  coverElement.style.backgroundImage = `url('${covers[currentCover]}')`;
}

setInterval(rotateCover, 20000);
