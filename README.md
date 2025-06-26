
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
git clone https://github.com/RandomForestPanda/FreeHandsControl.git
cd FreeHandsControl
pip install -r requirements.txt
```

## Requirements

- mediapipe
- opencv-python
- numpy
- pyobjc (for macOS system controls)


## Usage

### Volume Control
```bash
python -m FreeHandsControl.volume
```

### Zoom Control
```bash
python -m FreeHandsControl.zoom
```

### Brightness Control (Coming Soon)
```bash
python -m FreeHandsControl.brightness
```

## Safety Notice - Use with caution

This software directly modifies system settings on macOS. Use with caution:
- May affect system volume, display brightness, and application zoom levels
- Requires accessibility permissions
- Test in a controlled environment before regular use
- Not recommended for mission-critical systems

## Configuration

You can adjust parameters in the respective control files:
- `VolumeHandControl.py`: Adjust `[50,300]` range for volume sensitivity
- `ZoomHandcontrol.py`: Modify `length` thresholds for zoom sensitivity

## 🔐 Required macOS Permissions 

**⚠️ Warning**: Grant these permissions at your own risk. This software requires system-level access:

1. **Accessibility Access**  
   `System Preferences → Security & Privacy → Privacy → Accessibility`  
   *Allows volume/brightness control*

2. **Screen Recording** (optional for some versions)  
   `System Preferences → Security & Privacy → Privacy → Screen Recording`  
   *Required for application-specific zoom control*

3. **Terminal/IDE Permissions**  
   If running from terminal:  
   `System Preferences → Security & Privacy → Privacy → Full Disk Access`

### Security Considerations
- These permissions give the software system-modification capabilities
- Only install from trusted sources
- Review the [source code](https://github.com/RandomForestPanda/FreeHandsControl) before granting access
- Revoke permissions after use via the same settings panels
  


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Acknowledgments

- MediaPipe for the hand tracking solution
- AppleScript for macOS system control integration via OSAscript
