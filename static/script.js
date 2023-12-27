// Selecting the sidebar and buttons
const sidebarOpenBtn = document.querySelector("#sidebar-open");
const sidebarCloseBtn = document.querySelector("#sidebar-close");

// Function to hide the sidebar when the mouse leaves
const hideSidebar = () => {
  if (sidebar.classList.contains("hoverable")) {
    sidebar.classList.add("close");
  }
};

// Function to show the sidebar when the mouse enter
const showSidebar = () => {
  if (sidebar.classList.contains("hoverable")) {
    sidebar.classList.remove("close");
  }
};

// Function to show and hide the sidebar
const toggleSidebar = () => {
  sidebar.classList.toggle("close");
};


// Adding event listeners to buttons and sidebar for the corresponding actions

// sidebar.addEventListener("mouseleave", hideSidebar);
// sidebar.addEventListener("mouseenter", showSidebar);
// sidebarOpenBtn.addEventListener("click", toggleSidebar);
// sidebarCloseBtn.addEventListener("click", toggleSidebar);

// modal
$('.openmodale').click(function (e) {
  e.preventDefault();
  $('.modale').addClass('opened');
});
$('.closemodale').click(function (e) {
  e.preventDefault();
  $('.modale').removeClass('opened');
});