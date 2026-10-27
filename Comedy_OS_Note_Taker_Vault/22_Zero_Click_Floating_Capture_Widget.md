---
id: FEAT-TEXT-022
title: Zero-Click Floating Capture Widget
type: system-feature
status: active
tags: [comedy-os, widget, android, quick-capture, flutter]
---

# ⚡ Zero-Click Floating Capture Widget

> **The 1-Second Rule:** The comic shouldn't wait for splash screens, auth checks, or navigation trees.

## 1. Widget Trigger Surface
- **Lockscreen Glanceable Widget:** Single tap reveals a transient floating text overlay above the lockscreen.
- **Edge-Swipe Ribbon:** Pulling from the right bezel opens a floating scratchpad in PIP (Picture-in-Picture) over whatever the comedian was browsing.
- **Auto-IME Focus:** The virtual keyboard is programmatically requested on frame 0.

## 2. Technical Flutter Engine Optimization
```dart
class ZeroClickCaptureActivity extends StatefulWidget {
  @override
  _ZeroClickCaptureState createState() => _ZeroClickCaptureState();
}

class _ZeroClickCaptureState extends State<ZeroClickCaptureActivity> {
  final FocusNode _focusNode = FocusNode();
  final TextEditingController _textController = TextEditingController();

  @override
  void initState() {
    super.initState();
    // Immediate autofocus without waiting for build transition
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _focusNode.requestFocus();
    });
  }

  void _onAutoSave(String text) {
    if (text.trim().isEmpty) return;
    BitVaultRepository.quickInsert(rawContent: text);
  }
}
```
