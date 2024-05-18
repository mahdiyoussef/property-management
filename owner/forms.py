from utils.joi import joi,joiobject



create_owner = joi(
    dict(
        firstname = joiobject().string().required().maxlength(48).get(),
        lastname = joiobject().string().required().maxlength(48).get(),
        addressline1 = joiobject().string().maxlength(48).optional().get(),
        addressline2 = joiobject().string().maxlength(48).optional().get(),
        city = joiobject().string().maxlength(48).required().get(),
        country = joiobject().string().maxlength(4).optional().get(),
        managerid = joiobject().string().optional().get()
    )
)




