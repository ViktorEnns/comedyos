import { AudioEngine } from '../engines/AudioEngine';

export class AudioCaptureService {
  private engine = new AudioEngine();

  public beginCaptureSession(): void {
    this.engine.startRecording();
  }

  public endCaptureSession(): void {
    this.engine.stopRecording();
  }
}
