from src.monitoring.recorder import OccupancyRecorder

def test_recorder_creates_csv(tmp_path):
    path = tmp_path / "occupancy.csv"
    recorder = OccupancyRecorder(path)
    recorder.record(frame=30, elapsed_seconds=1.0, cattle_count=7)
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "timestamp,frame,elapsed_seconds,cattle_count"
    assert lines[1].endswith(",30,1.0,7")
