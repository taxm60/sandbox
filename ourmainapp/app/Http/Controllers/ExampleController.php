<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ExampleController extends Controller
{
    //
    public function homepage()
    {                
        $animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Zebra', 'Kangaroo', 'Panda', 'Penguin', 'Koala', 'Sloth'];

        return view('homepage', [ 'x' => $animals] );
    }

    public function about()
    {
        return ("<h1>ABOUT</h1><a href='/'>return HOME</a>");
    }
}
