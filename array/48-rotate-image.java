class Solution {
    public void rotate(int[][] matrix) {
        int l = matrix.length;

        /* Perform Tranposition */
        for (int i = 0; i < l; i++) {
            for (int j = i; j < l; j++){
                int cache = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = cache;
            }
        }
        
        /* Perform Horizontal Reversal */
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l / 2; j++){
                int cache = matrix[i][j];
                matrix[i][j] = matrix[i][l - 1 - j];
                matrix[i][l - 1 - j] = cache;
            }
        }
    }
}