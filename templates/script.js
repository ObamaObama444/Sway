window.onload = async () => {
    const cameraList = document.getElementById('camera-list');
    const cameras = await eel.get_available_cameras()();

    if (!cameras.length) {
        cameraList.innerHTML = "<p>Камеры не найдены</p>";
        return;
    }

    cameras.forEach(index => {
        const label = document.createElement('label');
        label.innerHTML = `<input type="checkbox" value="${index}"> Камера ${index}`;
        cameraList.appendChild(label);
    });
};

const startDetection = () => {
    const selectedCameras = [...document.querySelectorAll('#camera-list input:checked')]
        .map(input => parseInt(input.value));

    if (!selectedCameras.length) {
        alert("Выберите хотя бы одну камеру!");
        return;
    }

    const videoContainer = document.getElementById('video-container');
    videoContainer.innerHTML = '';

    selectedCameras.forEach(index => {
        const container = document.createElement('div');
        container.className = 'camera-container';

        const img = document.createElement('img');
        img.id = `video-${index}`;
        img.className = 'video-feed';
        img.alt = `Поток камеры ${index}`;

        const infoBox = document.createElement('div');
        infoBox.id = `info-${index}`;
        infoBox.className = 'info-box';
        infoBox.innerHTML = '<p>Загрузка данных...</p>';

        const toggleButton = document.createElement('button');
        toggleButton.textContent = 'Скрыть информацию';
        toggleButton.onclick = () =>
            infoBox.style.display = (infoBox.style.display === 'none') ? 'block' : 'none';

        const fullscreenButton = document.createElement('button');
        fullscreenButton.className = 'fullscreen-button';
        // Кнопка с иконкой полноэкранного режима (файл "1.jpg")
        fullscreenButton.innerHTML = '<img src="1.png" alt="Fullscreen">';
        fullscreenButton.onclick = () => toggleFullScreen(container);

        container.append(img, infoBox, toggleButton, fullscreenButton);
        videoContainer.appendChild(container);

        eel.start_camera(index);
    });
};

function toggleFullScreen(element) {
    if (!document.fullscreenElement) {
        element.requestFullscreen().catch(err =>
            console.error(`Ошибка при переходе в полноэкранный режим: ${err.message}`));
    } else {
        document.exitFullscreen();
    }
}

eel.expose(update_frame);
function update_frame(cameraIndex, frame, detectedData) {
    const imgElement = document.getElementById(`video-${cameraIndex}`);
    const infoBox = document.getElementById(`info-${cameraIndex}`);
    
    if (imgElement) {
        imgElement.src = frame;
    } else {
        console.error(`Ошибка: элемент видео ${cameraIndex} не найден.`);
    }

    if (infoBox) {
        if (detectedData && detectedData.length) {
            const details = detectedData
                .map(obj => `${obj.label}: ${obj.confidence.toFixed(2)}`)
                .join('<br>');
            infoBox.innerHTML = `<p>Обнаруженные объекты:</p><p>${details}</p>`;
        } else {
            infoBox.innerHTML = '<p>Объекты не обнаружены</p>';
        }
    }
}
