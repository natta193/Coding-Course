// TAKE-HOME PROJECT: Asteroid Drift
// After lesson C18 (Unity I – GameObjects and Scripts) - about 1–2 hours, in chunks over the next few days.
//
// Your first Unity mini-game: fly a ship through a drifting asteroid field. No physics yet
// – just Transform movement and your own scripts.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. A ship sprite with a ShipControls script: A/D rotate, W thrusts forward
//          (transform.up), with velocity that slowly drifts
//   [ ] 2. Wrap the ship around the screen edges (leave the right → appear on the left)
//   [ ] 3. An AsteroidSpawner that creates 8 asteroids from a prefab at random positions,
//          each with a random speed, direction and spin
//   [ ] 4. Asteroids wrap around the screen too – put the wrapping code in its own ScreenWrap
//          component and reuse it
//   [ ] 5. Camera follows nothing – the whole field fits on screen
//
// Stretch: Count how many seconds you survive without touching an asteroid (check
// distances in Update for now – physics comes next lesson).
//
// Bring it to the next session - working or stuck, both are fine.

using UnityEngine;
using UnityEngine.InputSystem;

public class ShipControls : MonoBehaviour
{
    public float turnSpeed = 180f;
    public float thrust = 6f;
}
