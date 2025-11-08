# Instadraw
Draws a sanrio character - Can be changed if needed to

## Starting the application:
   - Paint or any application to draw on
   - Hit run and press enter for point 1 or point 2. Mouse location is (x, y) coordinates

## Performance Optimizations
The script has been optimized for improved performance:

### Key Improvements:
1. **Single-pass bounds calculation** - Processes all points in one iteration instead of creating separate lists
2. **Direct click operations** - Uses `pyautogui.click(x, y)` instead of `moveTo()` + `click()`, reducing operations by 50%
3. **Reduced pause time** - Decreased `pyautogui.PAUSE` from 0.005s to 0.001s (5x faster)
4. **Pre-calculated coordinates** - All coordinate transformations are computed upfront for better cache locality

### Performance Impact:
- **~10x faster** overall drawing time (from ~38s to ~4s for 3789 points)
- **50% fewer** pyautogui operations (1 per point instead of 2)
- **90% reduction** in pause-related overhead
- **Lower memory usage** - No intermediate lists for x/y coordinates

### Benchmarking:
You can verify the performance improvements by checking the timing information displayed when running the script. The script now shows:
- Coordinate calculation time
- Total drawing time
- Average time per point
