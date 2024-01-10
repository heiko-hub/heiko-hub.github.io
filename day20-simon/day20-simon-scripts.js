let level = null;
let comSequence = null;
let colors = ["green", "red", "yellow", "blue"];
let checkIndex = null;
let bestLevel = null;

function showLevel() {
    $(".level-count").text(level);
}

function newColor() {
    let color = colors[Math.floor(Math.random() * 4)];
    comSequence.push(color);
    showColor(color);
}

function showColor(color) {
    $("#" + color).addClass("fade-out");
}

function animatePress(color) {
    let colorButton = $("#" + color);
    colorButton.addClass("pressed");
    setTimeout(function() {
        colorButton.removeClass("pressed");
    }, 400);
}

function addColorListeners() {
    $(".color-button").on("click", function() {
		let color = $(this).attr("id");
		animatePress(color);
        checkAnswer($(this));
    });
}

function newLevel() {
    level++;
    checkIndex = 0;
    showLevel();
    newColor();
}

function removeColorListeners() {
    $(".color-button").off();
}

function showBestLevel() {
    if (bestLevel === null || bestLevel === "-") {
        if (level !== 1) {
            bestLevel = level - 1;
        } else {
            bestLevel = "-";
        }
    } else if (level > bestLevel) {
        bestLevel = level - 1;
    }
    $(".best-level").text(`Best Level: ${bestLevel}`);
}

function gameOver() {
    removeColorListeners();
	showBestLevel();
    $(".start").removeClass("hide");
    $(".start").text("Restart");
}

function checkAnswer(colorClicked) {
    $(".color-button").removeClass("fade-out");
    if (colorClicked.hasClass(comSequence[checkIndex])) {
        if (checkIndex === comSequence.length - 1) {
            setTimeout(newLevel, 1000);
        } else {
            checkIndex++;
        }
    } else {
        gameOver();
    }
}

$(".start").on("click", function() {
    $(this).addClass("hide");
    level = 1;
    comSequence = [];
    checkIndex = 0;
    
    showLevel();
    newColor();
    addColorListeners();
});
