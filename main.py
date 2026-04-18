from fastapi import FastAPI
from pydantic import BaseModel
import os
from datetime import datetime

app = FastAPI()

class Clip(BaseModel):
    id: int
    title: str
    file_path: str
    duration: str

@app.get("/clips/")
async def read_clips():
    clips = [
        Clip(id=1, title="Birthday Party", file_path="/path/to/birthday.mp4", duration="00:03:45"),
        Clip(id=2, title="Hiking Adventure", file_path="/path/to/hiking.mp4", duration="00:10:20"),
        # Add more clips here...
    ]
    return clips

@app.post("/clips/")
async def create_clip(clip: Clip):
    # Save the clip to the database or file system
    # For this example, we'll just save it to a local variable
    saved_clip = clip.copy()
    saved_clip.id = len(os.listdir()) + 1
    saved_clip.file_path = f"/path/to/{saved_clip.title}.mp4"
    print(f"Clip {clip.title} created with ID {saved_clip.id}")
    return saved_clip

@app.put("/clips/{clip_id}/")
async def update_clip(clip_id: int, clip: Clip):
    # Find the clip to update
    for existing_clip in app.state.clips:
        if existing_clip.id == clip_id:
            # Update the clip's properties
            existing_clip.title = clip.title
            existing_clip.file_path = clip.file_path
            existing_clip.duration = clip.duration
            print(f"Clip {clip_id} updated")
            return existing_clip

@app.delete("/clips/{clip_id}/")
async def delete_clip(clip_id: int):
    # Find the clip to delete
    for i, clip in enumerate(app.state.clips):
        if clip.id == clip_id:
            del app.state.clips[i]
            print(f"Clip {clip_id} deleted")
            return {"message": "Clip deleted successfully"}

@app.get("/clips/{clip_id}/")
async def read_clip(clip_id: int):
    # Find the clip by ID
    for clip in app.state.clips:
        if clip.id == clip_id:
            return clip

@app.post("/clips/{clip_id}/merge/")
async def merge_clips(clip_id: int, merged_clip: Clip):
    # Find the original clips to merge
    original_clips = []
    for i, clip in enumerate(app.state.clips):
        if clip.id == clip_id:
            original_clips.append(clip)
    
    # Merge the clips
    merged_duration = datetime.strptime(original_clips[0].duration, "%H:%M:%S") + datetime.strptime(original_clips[1].duration, "%H:%M:%S")
    merged_duration = str(merged_duration).split(":")[0] + ":" + str(merged_duration).split(":")[1].split(".")[0]
    print(f"Clips {clip_id} merged into a new clip with duration {merged_duration}")
    return {"message": "Clips merged successfully"}

if __name__ == "__main__":
    app.state.clips = []
    uvicorn.run(app, host="0.0.0.0", port=8000)