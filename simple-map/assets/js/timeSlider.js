require(["esri/widgets/TimeSlider"], function(TimeSlider) {
    const timeSlider = new TimeSlider({
        container: "timeSliderDiv",
        view: view,
        fullTimeExtent: {
            start: new Date(2000, 0, 1),
            end: new Date(2024, 0, 1)
        },
        playRate: 500 // Speed of time animation
    });
    view.ui.add(timeSlider, "bottom-left");
});
