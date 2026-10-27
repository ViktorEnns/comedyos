import { AudioCaptureService } from '../services/AudioCaptureService';

export class CaptureDrawer {
  private service = new AudioCaptureService();

  public onRecordButtonClick(): void {
    this.service.beginCaptureSession();
  }
}
