import { CaptureDrawer } from './components/CaptureDrawer';
export * from './types/joke';

export function bootstrapApp(): void {
  const drawer = new CaptureDrawer();
  drawer.onRecordButtonClick();
  console.log("Comedy OS App started.");
}

