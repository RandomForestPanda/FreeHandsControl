
# Gestify : FreeHandsControl

![Gesture Control](https://img.shields.io/badge/Gesture-Control-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-green)
![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intuitive camera-based gesture control system for macOS that enables touchless control of system functions like volume, zoom, and brightness through hand gestures.

## Features

- **Volume Control**: Adjust system volume by pinching thumb and index finger
- **Zoom Control**: Zoom in/out in applications using hand gestures
- **Brightness Control**: Control display brightness with hand movements
- **Real-time Processing**: Low-latency hand tracking with MediaPipe
- **Customizable**: Adjust sensitivity and control ranges to your preference

## Installation

### Prerequisites
- Python 3.7+
- macOS (Windows support coming soon)
- Webcam 



### Install from source
```bash
git clone https://github.com/yourusername/Gestify.git
cd Gestify
pip install -r requirements.txt
```

## Usage

### Volume Control
```bash
python -m gestify.volume
```

### Zoom Control
```bash
python -m gestify.zoom
```

### Brightness Control (Coming Soon)
```bash
python -m gestify.brightness
```

## Configuration

You can adjust parameters in the respective control files:
- `VolumeHandControl_no_drawing.py`: Adjust `[50,300]` range for volume sensitivity
- `zoomHandcontrol.py`: Modify `length` thresholds for zoom sensitivity

## Requirements

- mediapipe
- opencv-python
- numpy
- pyobjc (for macOS system controls)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Acknowledgments

- MediaPipe for the hand tracking solution
- AppleScript for macOS system control integration via OSAscript
```
