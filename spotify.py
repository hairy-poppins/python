import spotipy
import os
import customtkinter as ctk
from spotipy.oauth2 import SpotifyOAuth
import threading

# Spotify API credentials
CLIENT_ID = "7e0e1e753651455692953fad203065ed"
CLIENT_SECRET = "f4ad38155e2b49ddbe6c1e4670d59eda"
REDIRECT_URI = "http://127.0.0.1:8000/callback"
SCOPE = "user-top-read"

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SpotifyTopTracksApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Spotify Top Tracks")
        self.root.geometry("600x700")
        
        self.sp = None
        self.setup_ui()
        self.authenticate()
        
    def setup_ui(self):
        # Title
        ctk.CTkLabel(
            self.root, 
            text="Your Top Spotify Tracks",
            font=("Arial", 24, "bold")
        ).pack(pady=20)
        
        # Time range selector
        self.time_range_var = ctk.StringVar(value="long_term")
        
        range_frame = ctk.CTkFrame(self.root)
        range_frame.pack(pady=10)
        
        ctk.CTkLabel(range_frame, text="Time Range:", font=("Arial", 14)).pack(side="left", padx=10)
        
        ctk.CTkSegmentedButton(
            range_frame,
            values=["Last 4 Weeks", "Last 6 Months", "All Time"],
            variable=self.time_range_var,
            command=self.on_time_range_change
        ).pack(side="left", padx=10)
        
        # Map display text to API values
        self.time_range_map = {
            "Last 4 Weeks": "short_term",
            "Last 6 Months": "medium_term",
            "All Time": "long_term"
        }
        self.time_range_var.set("All Time") # default to all time
        
        # Scrollable frame for tracks
        self.tracks_frame = ctk.CTkScrollableFrame(self.root, width=550, height=500)
        self.tracks_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        
        
    def on_time_range_change(self, value):
        self.load_tracks()
        
    def authenticate(self):
        def auth_thread():
            try:
                # Clear old cache
                if os.path.exists(".cache"):
                    os.remove(".cache")
                
                # Set up Spotify API
                self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                    client_id=CLIENT_ID,
                    client_secret=CLIENT_SECRET,
                    redirect_uri=REDIRECT_URI,
                    scope=SCOPE,
                    open_browser=True
                ))
                
                # Test connection
                self.sp.current_user()
                
                # Load tracks
                self.root.after(0, self.load_tracks)
                
            except Exception as e:
                self.root.after(0, lambda: self.status_label.configure(text=f"Authentication failed: {str(e)}"))
        
        threading.Thread(target=auth_thread, daemon=True).start() # start auth in the background
        
    def load_tracks(self):
        
            
        # Clear existing tracks
        for widget in self.tracks_frame.winfo_children():
            widget.destroy()
        
        
        def load_thread():
            try:
                time_range = self.time_range_map[self.time_range_var.get()]
                tracks = self.sp.current_user_top_tracks(limit=20, time_range=time_range)
                self.display_tracks(tracks['items'])
            except Exception as e:
                self.status_label.configure(text=f"Error: {str(e)}")
        
        threading.Thread(target=load_thread, daemon=True).start() # load tracks in background
        
    def display_tracks(self, tracks):
        for i, track in enumerate(tracks, start=1):
            track_name = track['name']
            
            artists_list = []
            for artist in track['artists']:
                artists_list.append(artist['name'])
            artists = ", ".join(artists_list)
            
            # Track frame
            frame = ctk.CTkFrame(self.tracks_frame, corner_radius=10)
            frame.pack(fill="x", padx=5, pady=5)
            
            # Rank
            ctk.CTkLabel(
                frame,
                text=f"{i}",
                font=("Arial", 16, "bold"),
                width=40
            ).pack(side="left", padx=10)
            
            # Track info
            info_frame = ctk.CTkFrame(frame, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            
            ctk.CTkLabel(
                info_frame,
                text=track_name,
                font=("Arial", 13, "bold"),
                anchor="w"
            ).pack(anchor="w")
            
            ctk.CTkLabel(
                info_frame,
                text=artists,
                font=("Arial", 11),
                text_color="gray",
                anchor="w"
            ).pack(anchor="w")
        
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SpotifyTopTracksApp()
    app.run()