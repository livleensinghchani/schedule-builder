var setDay = document.getElementById("DayType");
var buttonList = document.querySelectorAll(".dayButtons span");
var srcTime = new Date();
var dayToday = srcTime.getDay();
dayToday -= dayToday;
var selectDay = dayToday;
var weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
UpdateDay();
buttonList.forEach(function (element) {
    element.addEventListener("click", function () {
        selectDay = element.id == "btnLeft" ? selectDay - 1 : selectDay + 1;
        UpdateDay();
    });
});
function UpdateDay() {
    if (selectDay < 0) {
        selectDay = 4;
    }
    else if (selectDay > 4) {
        selectDay = 0;
    }
    setDay.innerText = weekDay[selectDay];
}
