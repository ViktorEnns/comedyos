export class AudioEngine {
  public startRecording(): void {
    console.log("AudioEngine: low-level hardware stream initialized.");
  }

  public stopRecording(): void {
    console.log("AudioEngine: stream halted.");
  }
}
