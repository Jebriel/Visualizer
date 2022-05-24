
# Client_ID = '53bdccda641245829c9daea6fc878abb'
# Client_Secret = 'eb843de56192411e9af97979b969a1f3'

# https://accounts.spotify.com/authorize?client_id=53bdccda641245829c9daea6fc878abb&response_type=code&redirect_uri=https%3A%2F%2Fgithub.com%2FJebriel%2F&2F

# 53bdccda641245829c9daea6fc878abb:eb843de56192411e9af97979b969a1f3
# NTNiZGNjZGE2NDEyNDU4MjljOWRhZWE2ZmM4NzhhYmI6ZWI4NDNkZTU2MTkyNDExZTlhZjk3OTc5Yjk2OWExZjM=

# curl -H "Authorization: Basic NTNiZGNjZGE2NDEyNDU4MjljOWRhZWE2ZmM4NzhhYmI6ZWI4NDNkZTU2MTkyNDExZTlhZjk3OTc5Yjk2OWExZjM=" -d grant_type=authorization_code -d code=AQCDWEx-HXnBdkGFCweiesVCTI1mFXMDwb9bYCDpl2IccMFxF1SjPOyh5UfVpe-MI-tgZ3N1bIsJAQItEjXxX6gbWRl0kszwZWUBexVTi3LYxxAFMfRP2QuDCifPHSp7PWJPGu3EW1doz5vUOCm2wHq7wc02njFNGMLbImqhcg -d redirect_uri=https%3A%2F%2Fgithub.com%2FJebriel%2F https://accounts.spotify.com/api/token

stuff = {"access_token":"BQDI1h4rqIshBrVWGqfmYtETZb7YcAu_mdjIkmQ78j5gTeSWfIClhztG8AIkZOEmQcOuuXb9L1IHaQBw6K0ycNLSdDFzL8xVZvmLaEurqGkRdk85kubWYpPmU9hxIakIFR-cbJ1Mnl91",
"token_type":"Bearer",
"expires_in":3600,
"refresh_token":"AQB_11-9lc2ElYTLjQSv1mscBRWtCx--kqXNUFx5ZzoYQ6WYVF_cHPASC6A3w0lFaFsyUpyucQIBPg6p_Bdimq-WdsnMTKJLBgDCQFz0y4K8wxtdX-PrgzmAmNRILh9SIgM"}

spotify_token = stuff['access_token']
spotify_user_id = 'tehag1'
playlist_id = '6AZmhUUSzUszsJa31LD47w'
