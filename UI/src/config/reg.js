export const idReg = /^[a-z0-9\-_]{5,20}$/;
export const pwReg = /^^(?=.*\d{1,20})(?=.*[~`!@#$%\^&*()-+=]{1,20})(?=.*[a-z]{1,20})(?=.*[A-Z]{1,20}).{8,20}$/;
export const phReg = /^01(0|1|[6-9])-([0-9]{4})-([0-9]{4})$/;
export const nameReg = /^[가-힣a-zA-z0-9]{1,50}$/;
export const engNameReg = /^[a-z]{1,100}$/;
export const telReg = /^(0[1-6][0-4]?)-([0-9]{3,4})-([0-9]{4})$/;
export const urlReg = /^(https?:\/\/)(([a-z0-9\-]+)\.)+[a-z0-9]{2,4}$/;
