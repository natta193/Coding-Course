// TAKE-HOME PROJECT: Mini Platformer Level
// After lesson C19 (Unity II – Physics, Prefabs and UI) - about 2 hours, in chunks over the next few days.
//
// Build one complete platformer level using physics, triggers, prefabs and UI.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. Use the PlatformerPlayer script from the lesson; build a level from Ground-tagged
//          platforms (with gaps!)
//   [ ] 2. Coins (trigger + Coin script) scattered around; the score shows in a TextMeshPro
//          label
//   [ ] 3. Spikes (trigger, tag "Hazard") and a fall zone below the level that send you back
//          to the last checkpoint
//   [ ] 4. A Checkpoint trigger that stores the player's respawn position
//   [ ] 5. A goal flag that shows "Level complete! X coins in Y seconds" and freezes time
//
// Stretch: Add a moving platform (Kinematic Rigidbody2D moved with MovePosition between
// two points) that carries the player.
//
// Bring it to the next session - working or stuck, both are fine.

using UnityEngine;

public class Respawner : MonoBehaviour
{
    public Vector3 respawnPoint;
}
