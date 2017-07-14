/**
 * Created by myMac-01 on 17/7/11.
 */
$(function () {

    var error_name = false;
    var error_pwd = false;
    var error_rempwd = false;

    $('.name_input').blur(function(){
        check_name();
    });
    $('.pass_input').blur(function () {
        check_pwd();
    });



    function check_name() {
        var len = $('.name_input').val().length;

        if (len == 0){
            $('.user_error').html('请填写用户名').show();
            error_name = true;

        }else {
            error_name = false;
        }

    }

    function check_pwd() {
        var len = $('.pass_input').val().length;
        if (len == 0) {
            $('.pwd_error').html('请输入密码').show();
            error_pwd = true;
        }else {
            error_pwd = false;
        }

    }

    $('.form_input').submit(function () {
        check_pwd();
        check_name();

        if (error_name == false && error_pwd == false){

            return true;
        }else {

            return false;
        }

    })








})